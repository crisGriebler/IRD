SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[CalcularRendimentoAtivos]
AS
BEGIN
    -- Metadata
    /*
        Criado por: Jefferson Moraes
        Data de criação: 06/01/2025
        Objetivo: Calcular os rendimentos diários de ativos financeiros com base nas posições, movimentações, IR isento e dividendos.
        Detalhes:
        - Filtro para ativos com CalculoPosicaoId = 1.
        - Converte valores entre moedas BRL e USD.
        - Calcula rendimentos considerando posição anterior e proventos.
        - Insere os resultados na tabela RendimentoDiarioAtivoTeste.
    */
    SET NOCOUNT ON;
    SET STATISTICS TIME ON;
    -- Variáveis de Log
    DECLARE @DataInicio DATETIME = GETDATE();
    DECLARE @DataFim DATETIME;

    PRINT 'Início do cálculo de rendimentos por ativos: ' + CONVERT(VARCHAR, @DataInicio);

 BEGIN TRY
 -------------------------------------------------------------------------------------------------------------
        -- Início da Transação

        BEGIN TRAN;
        -- Lógica Principal
 WITH CotacaoDolar AS (
    SELECT 
        p.Data, 
        p.Valor AS CotacaoDolar
    FROM Precificacao p
    INNER JOIN Moeda m ON m.Id = p.MoedaId
    WHERE p.EhMoeda = 1 AND m.CodigoIso = 'USD'
    AND p.Valor <> 0
),
AtivosParaCalculo AS (
    SELECT 
    a.Id,
    a.Nome,
    a.TipoAtivo,
    a.LocalId
    FROM Ativo a 
    JOIN SubClasse sub ON a.SubClasseId = sub.Id
    WHERE sub.CalculoPosicaoId = 1
),
Movimentacoes AS (
    SELECT 
        m.ClienteId,
        m.CustodiaId,
        m.AtivoId,
        m.DataCotizacao AS Data,
        SUM(CASE 
            WHEN m.TipoMovimentacaoId IN (2,3,8,9,12,17,18,19,20,21,26,31,32) THEN m.Valor
            ELSE 0 END) AS TotalMovimentos
    FROM Movimentacao m
    INNER JOIN AtivosParaCalculo a ON m.AtivoId = a.Id
    GROUP BY m.ClienteId, m.CustodiaId, m.AtivoId, m.DataCotizacao
),

IrIsento AS (
    SELECT
        ir.ClienteId,
        ir.CustodiaId,
        ir.AtivoId,
        ir.Data,
        SUM(ir.Posicao) AS TotalIrIsento
    FROM IrIsentoDiario ir
    INNER JOIN AtivosParaCalculo a ON ir.AtivoId = a.Id
    GROUP BY ir.ClienteId, ir.CustodiaId, ir.AtivoId, ir.Data
),
Dividendos AS (
    SELECT
        d.ClienteId,
        d.CustodiaId,
        d.AtivoId,
        d.Data,
        SUM(d.Valor) AS TotalDividendos
    FROM IrIsentoDividendos d
    INNER JOIN AtivosParaCalculo a ON d.AtivoId = a.Id
    GROUP BY d.ClienteId, d.CustodiaId, d.AtivoId, d.Data
),
PosicoesComAnterior AS (
    SELECT 
        p.ClienteId,
        p.CustodiaId,
        p.AtivoId,
        p.DataPosicao,
        p.ValorPosicao,
        p.ValorPosicaoBrl,
        p.ValorPosicaoUsd,
        LAG(p.ValorPosicao) OVER (PARTITION BY p.ClienteId, p.CustodiaId, p.AtivoId ORDER BY p.DataPosicao) AS ValorPosicaoAnterior,
        LAG(p.ValorPosicaoBrl) OVER (PARTITION BY p.ClienteId, p.CustodiaId, p.AtivoId ORDER BY p.DataPosicao) AS ValorPosicaoAnteriorBrl,
        LAG(p.ValorPosicaoUsd) OVER (PARTITION BY p.ClienteId, p.CustodiaId, p.AtivoId ORDER BY p.DataPosicao) AS ValorPosicaoAnteriorusd
    FROM PosicaoClienteAtivo p
    INNER JOIN AtivosParaCalculo a ON p.AtivoId = a.Id
),
ValoresConvertidos AS (
    SELECT
        p.ClienteId,
        p.CustodiaId,
        p.AtivoId,
        p.DataPosicao,
        m.TotalMovimentos AS Movimentos,
        -- Conversão de Movimentos
        CASE 
            WHEN a.LocalId = 2 THEN m.TotalMovimentos * COALESCE(cd.CotacaoDolar, 1)
            ELSE m.TotalMovimentos
        END AS MovimentosBrl,
        CASE 
            WHEN a.LocalId = 1 THEN m.TotalMovimentos / COALESCE(cd.CotacaoDolar, 1)
            ELSE m.TotalMovimentos
        END AS MovimentosUsd,
        ir.TotalIrIsento AS IrIsento,
        -- Conversão de IR Isento
        CASE 
            WHEN a.LocalId = 2 THEN ir.TotalIrIsento * COALESCE(cd.CotacaoDolar, 1)
            ELSE ir.TotalIrIsento
        END AS IrIsentoBrl,
        CASE 
            WHEN a.LocalId = 1 THEN ir.TotalIrIsento / COALESCE(cd.CotacaoDolar, 1)
            ELSE ir.TotalIrIsento
        END AS IrIsentoUsd,
        d.TotalDividendos as Dividendos,
        -- Conversão de Dividendos
        CASE 
            WHEN a.LocalId = 2 THEN d.TotalDividendos * COALESCE(cd.CotacaoDolar, 1)
            ELSE d.TotalDividendos
        END AS DividendosBrl,
        CASE 
            WHEN a.LocalId = 1 THEN d.TotalDividendos / COALESCE(cd.CotacaoDolar, 1)
            ELSE d.TotalDividendos
        END AS DividendosUsd
    FROM PosicoesComAnterior p
    LEFT JOIN Movimentacoes m ON p.ClienteId = m.ClienteId AND p.CustodiaId = m.CustodiaId AND p.AtivoId = m.AtivoId AND p.DataPosicao = m.Data
    LEFT JOIN IrIsento ir ON p.ClienteId = ir.ClienteId AND p.CustodiaId = ir.CustodiaId AND p.AtivoId = ir.AtivoId AND p.DataPosicao = ir.Data
    LEFT JOIN Dividendos d ON p.ClienteId = d.ClienteId AND p.CustodiaId = d.CustodiaId AND p.AtivoId = d.AtivoId AND p.DataPosicao = d.Data
    LEFT JOIN CotacaoDolar cd ON p.DataPosicao = cd.Data
    LEFT JOIN AtivosParaCalculo a ON p.AtivoId = a.Id
),
RendimentoAtivos AS (
    SELECT 
        p.ClienteId,
        p.CustodiaId,
        p.AtivoId,
        p.DataPosicao,
        -- Cálculo do Rendimento Original
        CASE
            WHEN COALESCE(p.ValorPosicaoAnterior, 0) = 0 THEN
                (p.ValorPosicao + COALESCE(vc.Movimentos, 0))
            ELSE
                (p.ValorPosicao 
                 + COALESCE(vc.Movimentos, 0)
                 + COALESCE(vc.IrIsento, 0)
                 + COALESCE(vc.Dividendos, 0))
                - (COALESCE(p.ValorPosicaoAnterior, 0)
                   + COALESCE(LAG(vc.IrIsento) OVER (PARTITION BY p.ClienteId, p.CustodiaId, p.AtivoId ORDER BY p.DataPosicao), 0))
        END AS RendimentoOriginal,
        -- Cálculo do Rendimento em BRL
        CASE
            WHEN COALESCE(p.ValorPosicaoAnteriorBrl, 0) = 0 THEN
                (p.ValorPosicaoBrl + COALESCE(vc.MovimentosBrl, 0))
            ELSE
                (p.ValorPosicaoBrl 
                 + COALESCE(vc.MovimentosBrl, 0)
                 + COALESCE(vc.IrIsentoBrl, 0)
                 + COALESCE(vc.DividendosBrl, 0))
                - (COALESCE(p.ValorPosicaoAnteriorBrl, 0)
                   + COALESCE(LAG(vc.IrIsentoBrl) OVER (PARTITION BY p.ClienteId, p.CustodiaId, p.AtivoId ORDER BY p.DataPosicao), 0))
        END AS RendimentoBrl,
        -- Cálculo do Rendimento em USD
        CASE
            WHEN COALESCE(p.ValorPosicaoAnteriorUsd, 0) = 0 THEN
                (p.ValorPosicaoUsd + COALESCE(vc.MovimentosUsd, 0))
            ELSE
                (p.ValorPosicaoUsd 
                 + COALESCE(vc.MovimentosUsd, 0)
                 + COALESCE(vc.IrIsentoUsd, 0)
                 + COALESCE(vc.DividendosUsd, 0))
                - (COALESCE(p.ValorPosicaoAnteriorUsd, 0)
                   + COALESCE(LAG(vc.IrIsentoUsd) OVER (PARTITION BY p.ClienteId, p.CustodiaId, p.AtivoId ORDER BY p.DataPosicao), 0))
        END AS RendimentoUsd
    FROM PosicoesComAnterior p
    LEFT JOIN ValoresConvertidos vc ON p.ClienteId = vc.ClienteId AND p.CustodiaId = vc.CustodiaId AND p.AtivoId = vc.AtivoId AND p.DataPosicao = vc.DataPosicao
)

INSERT INTO RendimentoDiarioAtivo (Id, ClienteId, AtivoId, CustodiaId, ValorOriginal, ValorBrl, ValorUsd, Data, CreatedAt, UpdatedAt)
SELECT 
    NEWID(), ClienteId, AtivoId, CustodiaId, RendimentoOriginal, RendimentoBrl, RendimentoUsd, DataPosicao, GETDATE(), GETDATE()
FROM RendimentoAtivos
        -- Finaliza Transação
COMMIT;
 
        -- Fim da Lógica de Transação
-------------------------------------------------------------------------------------------------------------
        SET @DataFim = GETDATE();
        PRINT 'Cálculo concluído. Tempo total: ' + CONVERT(VARCHAR, DATEDIFF(SECOND, @DataInicio, @DataFim)) + ' segundos.';

    END TRY
    BEGIN CATCH
        -- Rollback em Caso de Erro
        ROLLBACK;
        PRINT 'Erro no processamento: ' + ERROR_MESSAGE();
    END CATCH;
    SET STATISTICS TIME OFF;
END;
GO
