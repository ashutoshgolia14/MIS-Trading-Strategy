import argparse

from app.wiring.runtime import run_runtime
from app.backtest.runner import run_backtest


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["live", "backtest"], required=True)

    args = parser.parse_args()

    if args.mode == "live":
        run_runtime(
            price_stream=[100, 105, 111, 120],
            brick_size=10
        )

    elif args.mode == "backtest":
        run_backtest(
            csv_path="data/sample_prices.csv",
            brick_size=10
        )


if __name__ == "__main__":
    main()