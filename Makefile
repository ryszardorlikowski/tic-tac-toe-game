docker-build:
	docker compose build

docker-up:
	docker compose up -d

docker-logs:
	docker compose logs -f

docker-down:
	docker compose down


run-backend-tests:
	docker exec tic_tac_toe_game pytest tests/ -v -s