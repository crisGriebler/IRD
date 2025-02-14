SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[CalcularRendimentoContaCorrenteEcustos]
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
ContaCorrenteParaCalculo AS (
    SELECT 
        a.Id,
        a.Nome,
        a.TipoAtivo,
        a.LocalId
    FROM Ativo a 
    JOIN SubClasse sub ON a.SubClasseId = sub.Id
    WHERE sub.CalculoPosicaoId = 2
),
CustosParaCalculo AS (
    SELECT 
        a.Id,
        a.Nome,
        a.TipoAtivo,
        a.LocalId
    FROM Ativo a 
    JOIN SubClasse sub ON a.SubClasseId = sub.Id
    WHERE sub.CalculoPosicaoId = 3
),
MovimentacoesContaCorrente AS (
    SELECT 
        m.ClienteId,
        m.CustodiaId,
        m.DataLiquidacao AS Data,
        cc.LocalId,
        SUM(m.Valor) AS Movimentos,
           CASE 
            WHEN cc.LocalId = 2 THEN  SUM(m.Valor) * COALESCE(cd.CotacaoDolar, 1)
            ELSE  SUM(m.Valor)
        END AS MovimentosBrl,
        CASE 
            WHEN cc.LocalId = 1 THEN  SUM(m.Valor) / COALESCE(cd.CotacaoDolar, 1)
            ELSE SUM(m.Valor)
        END AS MovimentosUsd
    FROM Movimentacao m
     INNER JOIN ContaCorrenteParaCalculo cc ON cc.Id = m.AtivoId
     INNER JOIN CotacaoDolar cd ON m.DataLiquidacao = cd.Data
    WHERE m.TipoMovimentacaoId IN (26,33) --(26, 33)
    GROUP BY m.ClienteId, m.CustodiaId, cc.LocalId, m.DataLiquidacao,cd.CotacaoDolar
),
MovimentacoesCustos AS (
    SELECT 
        m.ClienteId,
        m.CustodiaId,
        m.AtivoId,
        m.DataLiquidacao AS Data,
        c.LocalId,
        SUM(m.Valor) AS Movimentos,
           CASE 
            WHEN c.LocalId = 2 THEN  SUM(m.Valor) * COALESCE(cd.CotacaoDolar, 1)
            ELSE  SUM(m.Valor)
        END AS MovimentosBrl,
        CASE 
            WHEN c.LocalId = 1 THEN  SUM(m.Valor) / COALESCE(cd.CotacaoDolar, 1)
            ELSE SUM(m.Valor)
        END AS MovimentosUsd
    FROM Movimentacao m
    INNER JOIN CustosParaCalculo c ON c.Id = m.AtivoId
    LEFT JOIN CotacaoDolar cd ON m.DataLiquidacao = cd.Data
    WHERE m.TipoMovimentacaoId IN (34) -- Taxas/Fees Custos
    GROUP BY m.ClienteId, m.CustodiaId,m.AtivoId,c.LocalId, m.dataliquidacao, cd.CotacaoDolar
),
PosicoesComAnteriorContaCorrente AS (
    SELECT 
        p.ClienteId,
        p.CustodiaId,
        p.AtivoId,
        p.DataPosicao
    FROM PosicaoClienteAtivo p
    INNER JOIN ContaCorrenteParaCalculo cc ON p.AtivoId = cc.Id
),
PosicoesComAnteriorCustos AS (
    SELECT 
        p.ClienteId,
        p.CustodiaId,
        p.AtivoId,
        p.DataPosicao
    FROM PosicaoClienteAtivo p
    INNER JOIN CustosParaCalculo cc ON p.AtivoId = cc.Id
),

RendimentoContaCorrente AS (
    SELECT 
        p.ClienteId,
        p.CustodiaId,
        p.AtivoId,
        p.DataPosicao,
        -- Rendimento Original
      COALESCE(mcc.Movimentos, 0) AS RendimentoOriginal,
        -- Rendimento em BRL
       COALESCE(mcc.MovimentosBrl, 0) AS RendimentoBrl,
        -- Rendimento em USD
       COALESCE(mcc.MovimentosUsd, 0) AS RendimentoUsd
    FROM PosicoesComAnteriorContaCorrente p
    LEFT JOIN MovimentacoesContaCorrente mcc 
    ON p.ClienteId = mcc.ClienteId 
    AND p.CustodiaId = mcc.CustodiaId 
    AND p.DataPosicao = mcc.Data
),
RendimentoCustos AS (
    SELECT 
        p.ClienteId,
        p.CustodiaId,
        p.AtivoId,
        p.DataPosicao,
        -- Rendimento Original
        COALESCE(mc.Movimentos, 0) AS RendimentoOriginal,
        -- Rendimento em BRL
        COALESCE(mc.MovimentosBrl, 0) AS RendimentoBrl,
        -- Rendimento em USD
        COALESCE(mc.MovimentosUsd, 0) AS RendimentoUsd
    FROM PosicoesComAnteriorCustos p
    LEFT JOIN MovimentacoesCustos mc
     ON p.ClienteId = mc.ClienteId 
     AND p.CustodiaId = mc.CustodiaId 
     AND mc.AtivoId = p.AtivoId 
     AND p.DataPosicao = mc.Data
)

-- Consolidação dos Resultados
INSERT INTO RendimentoDiarioAtivo (Id, ClienteId, AtivoId, CustodiaId, ValorOriginal, ValorBrl, ValorUsd, Data, CreatedAt, UpdatedAt)
SELECT 
    NEWID(), ClienteId, AtivoId, CustodiaId, RendimentoOriginal, RendimentoBrl, RendimentoUsd, DataPosicao, GETDATE(), GETDATE()
FROM RendimentoContaCorrente
UNION ALL
SELECT 
    NEWID(), ClienteId, AtivoId, CustodiaId, RendimentoOriginal, RendimentoBrl, RendimentoUsd, DataPosicao, GETDATE(), GETDATE()
FROM RendimentoCustos
        -- Finaliza Transação
        COMMIT;

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
