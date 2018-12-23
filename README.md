
### Criar diretório exclusivo para o bot de notificações operar ###

	$ mkdir /home/usuario/bot/

### Copiar página que será verificada ####

A página que será verificada deve ser copiada inicialmente para o script começar a operar. A cópia pode ser feita através do comando:

	$ curl http://www.pagina.com.br/ > /home/usuario/bot/pg.txt

### Atualizar diretorio no script na variável path

	$ path = "/home/usuario/bot/"

### Ativar bot do [Integram](https://integram.org/) no seu Telegram

Para ativar o bot do Integram, basta seguir o usuário @bullhorn_bot. Agora clique em start e copie a URL de identificação que será gerada. A URL deve ser adicionada à variável idbot conforme indicado abaixo:

	$ idbot = "https://integram.org/webhook/cHnEjEDNd2R"

### Criar execução programada no CRON para verificação de atualização na página ###

	$ crontab -e

Adicionar ao final do arquivo:
	
	*/5 * * * * python /home/joahannes/bot/atualiza.py

### FEITO :)
