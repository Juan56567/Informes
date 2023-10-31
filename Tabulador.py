from docx import Document

doc = Document("documento_modificado.docx")

# Recorre todas las tablas en el documento
for table in doc.tables:
    for i, row in enumerate(table.rows):
        for j, cell in enumerate(row.cells):
            # Reemplaza el contenido de la celda con el índice
            cell.text = f"{i}, {j}"

# Guarda el documento modificado
doc.save("documento_modificado.docx")

print("Reemplazo de celdas con índices completado con éxito.")
