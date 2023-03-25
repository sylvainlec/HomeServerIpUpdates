# Home Server Ip Updates
Send your public webserver IP through Telegram.
When your public IP changed and are not at home, this script will notify you so that you can update your IP on your DNS provider.

[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](http://forthebadge.com)  [![forthebadge](http://forthebadge.com/images/badges/powered-by-electricity.svg)](http://forthebadge.com)

## Warm up

Docker is recommended to run this project.

### Needed

Install Docker
Install docker-compose
Create or use existing Telegram bot and retrieve those two keys infos:
- Bot token
- Chat Id

### Installation

1) Place a .env file in he same folder as the docker-compose.yml
2) Create variable TELEGRAM_BOT_TOKEN in the .env file: TELEGRAM_BOT_TOKEN=MyTelegramBotToken
3) Create variable TELEGRAM_CHAT_ID in the .env file: TELEGRAM_CHAT_ID=MyTelegramChatId
4) Run the docker-compose command: docker-compose -f docker-compose.yml --build

## Versions
Listez les versions ici 
**Dernière version stable :** N/A
**Dernière version :** N/A

## Auteurs
* **Sylvain Lecornu** _alias_ [@sylvainlec](https://github.com/sylvainlec)