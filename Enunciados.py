diagnostico = {
    "bueno": "Tras realizar una evaluación exhaustiva, se ha constatado que el elemento en cuestión se encuentra en óptimas condiciones y cumple plenamente con los estándares y normativas establecidos. No presenta irregularidades",
    "cambio": {
        "corrosion": "Tras una exhaustiva inspección, se ha determinado que se requiere efectuar el reemplazo de la pieza debido a la presencia de corrosión en su superficie. La corrosión, resultado de la reacción química entre el material de la pieza y agentes externos, ha provocado un deterioro significativo que compromete su integridad estructural y funcionalidad. ",
        "tolerancia": "Tras un detallado proceso de diagnóstico, se ha constatado de manera inequívoca que la pieza en cuestión se encuentra fuera de los límites de tolerancia establecidos. En consecuencia, es imperativo llevar a cabo la sustitución de la misma, ya que su condición actual compromete su correcto funcionamiento y afecta su capacidad para cumplir con los requisitos y estándares exigidos.",
        "golpes": "Tras realizar una evaluación técnica exhaustiva, se ha determinado que la pieza en cuestión presenta evidentes signos de impactos fuertes, los cuales han afectado significativamente su integridad y rendimiento. Por consiguiente, se hace necesario proceder con el reemplazo de dicha pieza, ya que los golpes sufridos han comprometido su capacidad para cumplir con las funciones requeridas y los estándares establecidos.",
        "desprendimiento": "Tras una exhaustiva inspección técnica, se ha evidenciado de manera contundente el desprendimiento de cromo en la superficie de la pieza en cuestión. Este fenómeno representa una clara indicación de un deterioro significativo en el recubrimiento de cromo aplicado previamente. En vista de esto, resulta imprescindible llevar a cabo el reemplazo de la pieza, ya que el desprendimiento de cromo compromete tanto su apariencia estética como su resistencia a la corrosión y su capacidad de cumplir con los estándares de calidad exigidos.",
        "desgaste": "Tras un exhaustivo análisis técnico, se ha determinado que debido al desgaste significativo experimentado por la pieza en cuestión, se recomienda encarecidamente proceder a su sustitución. El deterioro observado en la pieza es evidente tanto a nivel visual como funcional, lo que indica una disminución en su rendimiento y confiabilidad. El desgaste acumulado ha afectado negativamente las propiedades estructurales y mecánicas de la pieza, comprometiendo su capacidad para cumplir con los requisitos operativos y de seguridad establecidos.",
        "rallas": "De acuerdo con el análisis técnico realizado, se hace imprescindible llevar a cabo la sustitución de la pieza en cuestión debido a la manifestación de rayas de considerable profundidad en su superficie. Estas marcas abrasivas y notorias representan un factor determinante que compromete significativamente tanto el funcionamiento fluido del componente como su capacidad para cumplir con los estándares de desempeño requeridos. ",
        "flexion": "Se ha determinado que es necesario realizar el reemplazo de la pieza debido a la presencia de deformación por flexión. Después de un análisis exhaustivo y pruebas de resistencia, se ha confirmado que la pieza ha experimentado una deformación significativa debido a fuerzas de flexión aplicadas en su entorno operativo.",
        "destruir": "Fue necesario proceder a la destrucción de la pieza debido a que la misma no pudo ser desensamblada siguiendo los métodos y procedimientos de desmontaje estándar. A pesar de los esfuerzos realizados, la pieza se encontraba tan integrada o soldada que cualquier intento adicional de desmontaje resultaría en daños irreparables o comprometería la integridad de otros componentes cercanos",
    },
    "rectificar": {
        "cromar": "Tras un análisis exhaustivo, se ha determinado la necesidad imperante de someter la pieza a un proceso de cromado debido a la presencia significativa de rallas o imperfecciones en su superficie. El trabajo del cilindro ha ocasionado un deterioro progresivo y visible en la estructura metálica de la pieza, comprometiendo tanto su resistencia como su funcionalidad.",
        "brillar": "Una vez finalizado el minucioso proceso de diagnóstico de la pieza, se ha determinado que es necesario llevar a cabo un procedimiento de pulido con el fin de restaurar su acabado original, eliminar cualquier imperfección superficial y mejorar significativamente su apariencia estética. Mediante este proceso de pulido, se aplicarán técnicas especializadas para eliminar cualquier rastro de desgaste, marcas o defectos que puedan haberse manifestado debido a condiciones de uso, daños externos o desgaste natural",
        "brunir": "Luego de un minucioso diagnóstico, se determina que es indispensable llevar a cabo el proceso de bruñido en la pieza en cuestión. Esta acción se hace necesaria para eliminar las irregularidades y asperezas presentes en su superficie, las cuales afectan de manera directa tanto la funcionalidad como la durabilidad del componente. El bruñido, mediante la utilización de abrasivos finos y técnicas de pulido específicas, permitirá obtener una superficie lisa, uniforme y libre de imperfecciones, restableciendo así las condiciones óptimas de deslizamiento",
        "deformacion": "Se ha determinado la necesidad de realizar la rectificación de la pieza debido a la presencia de deformación. Esta deformación, detectada mediante análisis dimensional y pruebas exhaustivas, ha comprometido la geometría y la precisión requeridas para el correcto funcionamiento de la pieza.",
        "rosca": "Tras realizar una evaluación detallada, se ha identificado que la rosca de la pieza presenta irregularidades y dimensiones fuera de tolerancia. Estas condiciones inadecuadas afectan negativamente la funcionalidad y seguridad del ensamblaje al que pertenece.",
    },
}

# cambios

bueno = diagnostico["bueno"]
cambioCorrosion = diagnostico["cambio"]["corrosion"]
cambioTolerancia = diagnostico["cambio"]["tolerancia"]
cambioGolpes = diagnostico["cambio"]["golpes"]
cambioDesprendimiento = diagnostico["cambio"]["desprendimiento"]
cambioDesgaste = diagnostico["cambio"]["desgaste"]
cambioRallas = diagnostico["cambio"]["rallas"]
cambioFlexion = diagnostico["cambio"]["flexion"]

# rectificados

rectiCromo = diagnostico["rectificar"]["cromar"]
rectiBrillar = diagnostico["rectificar"]["brillar"]
rectiBrunir = diagnostico["rectificar"]["brunir"]
rectiDeformacion = diagnostico["rectificar"]["deformacion"]
rectiRosca = diagnostico["rectificar"]["rosca"]
