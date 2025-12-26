from app.bootstrap import bootstrap

def main():
    mode = bootstrap()
    print(f"System started in {mode.value} mode")

if __name__ == "__main__":
    main()
