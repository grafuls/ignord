from ignord.cli import main


def test_main():
    main([])
    
def test_list():
    main({"--list": True})
    
def test_lang():
    main({"language": "python"})
