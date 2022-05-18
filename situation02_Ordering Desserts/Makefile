.PHONY: rasa env-up rasa-x

##### ENV
env-up:
	@echo "啟動環境 ..."
	@pipenv shell
	@echo "環境已啟動"

##### Rasa Actions
rasa-actions:
	@echo "請記得先執行 make env-up 進入虛擬環境"
	@echo "啟動 Rasa Actions ..."
	@rasa run actions

##### Rasa X
rasa-x:
	@echo "請記得先執行 make env-up 進入虛擬環境"
	@echo "啟動 Rasa X ..."
	@rasa x --enable-api
	
##### --ssl-certificate /etc/letsencrypt/live/sels.nkfust.edu.tw/fullchain.pem --ssl-keyfile /etc/letsencrypt/live/sels.nkfust.edu.tw/privkey.pem
