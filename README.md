
### Copiar página que será verificada ####

A página que será verificada deve ser copiada inicialmente para o script começar a operar. A cópia pode ser feita através do comando:

	$ curl http://www.pagina.com.br/ > pg.txt

### Criar diretório exclusivo para o bot de notificações operar ###

	$ mkdir /home/usuario/bot/

### Atualizar diretorio no script na variável path

	$ path = "/home/usuario/bot/"

### Ativar bot HORN no Telegram, pegar id e colar na variavel idbot no script

	$ idbot = "https://integram.org/webhook/cHnEjEDNd2R"

### Criar execução programada no CRON para verificação de atualização na página ###

	$ crontab -e

Adicionar ao final do arquivo:
	
	*/5 * * * * python /home/joahannes/bot/atualiza.py

### FEITO :)
