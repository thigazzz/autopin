classes: Image, Imagens, Tópicos, Topic

Imagem precisa de Imagens
Imagem precisa de um Scrapper
Topicos precisa de um Scrapper
Tópicos precisa de um Imagem

## Images
Estrutura de dados de Imagem:

{   
    id: int
    topic: str
    src: str
    name: str
}

### Image:
métodos:
get_images_from_topic(topic: Topic, ammount_of_images = 10) -> list(Imagens)
"""
Extrai dados de imagens de um tópico e retorna uma lista de imagens
"""

### Topic
Estrutura de dados de Topico:
{   
    name: str
    description: str
}

### Topics
Estrutura de dados de Topico:
{   
    name: Topic.name
    description: Topic.description
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