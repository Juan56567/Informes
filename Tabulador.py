from docx import Document

doc = Document("C:/Users/Lenovo/Desktop/PROYECTOS JUAN DIEGO/WORD/INFORME CHTZ.docx")

tables = doc.tables

# Recorre todas las tablas en el documento
for table in tables:
    for i, row in enumerate(table.rows):
        for j, cell in enumerate(row.cells):
            # Reemplaza el contenido de la celda con el índice
            cell.text = f"{tables.index(table)},{    i}, {j}"

# Guarda el documento modificado
doc.save("C:/Users/Lenovo/Desktop/PROYECTOS JUAN DIEGO/PYTHON/TAB CHTZ.docx")

print("Reemplazo de celdas con índices completado con éxito.")
