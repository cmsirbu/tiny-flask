from tinyflask import app


def test_http_root():
    """
    Test the / path works and returns the expected template.
    """

    response = app.test_client().get("/")

    rdata = response.data.decode("utf-8")

    assert response.status_code == 200
    assert "It's alive!" in rdata
