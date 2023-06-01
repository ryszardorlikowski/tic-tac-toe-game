docker-build:
	docker compose build

docker-up:
	docker compose up

docker-logs:
	docker compose logs

docker-down:
	docker compose down


run-backend-tests:
	docker exec tic_tac_toe_game pytest tests/ -v -s