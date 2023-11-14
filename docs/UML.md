classes: Imagens, Tópicos

Imagens precisa de um Scrapper
Topicos precisa de um Scrapper
Tópicos precisa de um Images

Estrutura de dados de Imagens:

{   
    id: int
    topic: str
    src: str
    name: str
}

métodos:
get_images_from_topic(topic, ammount_of_images = 10) -> list(Images)
"""
Extrai dados de imagens de um tópico e retorna uma lista de imagens
"""


Estrutura de dados de Topicos:
{   
    name: str
    description: str
    images: list(Image)
}

métodos:
show_recommended_topics() -> list(str)
"""
Mostra uma lista de tópicos que foram recomendados no site do Pinterest
"""

show_images_from_topic(topic: str) -> Topic
"""
Mostra um tópico e suas respectivas imagens
"""