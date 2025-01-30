solid state Tesla coil (SSTC)を矩形波インバータで駆動した時、うまくデッドタイムを設定することでZVSできるのでは？という基礎検討。
定常状態でインバータ出力をいきなりオープンにしたとき、寄生容量に加わる電圧がゼロボルトを横切ることができればZVSが可能。
-> LTspiceのファイル（tesla_HFSSTC_ZVS_condition_v1.asc, tesla_HFSSTC_ZVS_condition_v2.asc）

入力電圧をs領域で立式し、簡単にシミュレーションすることができるようにした。
-> pythonファイル（tesla_SSTC_step_response_v1.py）

計算過程
-> 画像, mathematicaのスクリプトをまとめたもの(keisan.txt)
