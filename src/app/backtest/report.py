def generate_report(recorder):
    print('Backtest Summary')
    print('----------------')
    print(f'Ticks processed: {recorder.ticks}')
    print(f'Executions:      {len(recorder.executions)}')
    for e in recorder.executions:
        print(f"{e['ts']} | {e['status']} | {e['fill_price']} | {e['reason']}")
