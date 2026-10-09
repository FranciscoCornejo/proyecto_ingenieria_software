from app import create_app

def test_home_and_all_modules(client):
    page = client.get("/")
    assert page.status_code == 200
    for module in ["ejemplo", *[f"grupo_{n:02}" for n in range(1, 10)]]:
        assert f"/modulos/{module}/".encode() in page.data
        assert client.get(f"/modulos/{module}/").status_code == 200

def test_routes_stay_inside_module():
    app = create_app()
    seen = set()
    for route in app.url_map.iter_rules():
        for method in route.methods - {"HEAD", "OPTIONS"}:
            assert (route.rule, method) not in seen
            seen.add((route.rule, method))
        owner = route.endpoint.split(".")[0]
        if owner.startswith("grupo_") or owner == "ejemplo":
            assert route.rule.startswith(f"/modulos/{owner}/")
            assert route.methods <= {"GET", "HEAD", "OPTIONS"}
