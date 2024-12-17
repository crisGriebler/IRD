from docx import Document

# Criação do documento Word
doc = Document()

# Título do documento
doc.add_heading('Governança de Low-Code com Power Apps', level=1)

# Adicionando os conteúdos em texto estruturado
doc.add_paragraph(
    "A governança eficiente de low-code com Power Apps é essencial para garantir segurança, conformidade e eficiência "
    "no uso da plataforma. O primeiro passo é estabelecer uma estrutura de governança que defina claramente os papéis e "
    "responsabilidades das diferentes partes envolvidas, incluindo os desenvolvedores cidadãos, a equipe de TI e os "
    "desenvolvedores profissionais. A criação de uma equipe de governança composta por membros da TI, compliance e "
    "áreas de negócios também é fundamental para supervisionar o uso adequado da plataforma."
)

doc.add_paragraph(
    "É importante desenvolver políticas de uso que limitem permissões e controlem quem pode criar e publicar aplicativos. "
    "Além disso, deve-se controlar o uso de conectores, principalmente em relação a dados sensíveis, e estabelecer regras "
    "de nomenclatura para facilitar a organização e o gerenciamento dos aplicativos criados."
)

doc.add_paragraph(
    "A implementação de ferramentas de monitoramento e auditoria é uma etapa crucial. Utilizar o Power Platform Admin "
   