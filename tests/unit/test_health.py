def test_health_returns_expected_payload(client) -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.text == '{"status":"ok","version":"0.1.0"}'
    assert response.json() == {"status": "ok", "version": "0.1.0"}
