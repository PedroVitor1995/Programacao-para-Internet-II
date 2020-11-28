# Programacao-para-Internet-II

# 1 - IP-API - https://ip-api.com/

    É uma API de consulta a localização de um IP
    
    O caminho base da API é
    http://ip-api.com/json/{query}
        {query}pode ser um único endereço IPv4 / IPv6 ou um nome de domínio. Se você não fornecer uma 
        consulta, o endereço IP atual será usado.
    
    Parâmetros de consulta (como campos personalizados e retorno de chamada JSONP) são anexados como 
    parâmetros de solicitação GET, por exemplo:
        http://ip-api.com/json/?fields=61439

----------------------------------------------------------------------------------------------------------

# 2 - Makeup API - https://makeup-api.herokuapp.com/

    É uma API de consulta produtos e filtre-os por marca, preço, categoria de produto, etiquetas e muito
    mais.

    O endpoint da versão atual da API é:
        http://makeup-api.herokuapp.com/api/v1/products.json
    
    Para pesquisar a marca “maybelline”, anexe 'brand = maybelline'. Por exemplo:
        http://makeup-api.herokuapp.com/api/v1/products.json?brand=maybelline

----------------------------------------------------------------------------------------------------------

# 3 - Data API - https://developer.dailymotion.com/api/

    É uma API que permite acessar dados sobre vídeos, usuários, comentários, etc.

    Cada objeto na API de dados do Dailymotion possui um identificador exclusivo (dentro de sua
    classe de objeto). Você pode acessar os campos de cada objeto, solicitando /<OBJECT_CLASS>/<OBJECT_ID>,
    onde <OBJECT_CLASS>pode ser video, user, playlist, etc.

