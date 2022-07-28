# Import the required Module
import tabula
# Read a PDF File
df = tabula.read_pdf("PLANO_DE_CURSO_2022_ENSINO_MEDIO_CIENCIAS_DA_NATUREZA_01.02.pdf", pages='all')[0]
# convert PDF into CSV
tabula.convert_into("PLANO_DE_CURSO_2022_ENSINO_MEDIO_CIENCIAS_DA_NATUREZA_01.02.pdf", "PLANO_DE_CURSO_2022_ENSINO_MEDIO_CIENCIAS_DA_NATUREZA_01.02.csv", output_format="csv", pages='all')
print(df)