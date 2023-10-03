from math import ceil

def calc_account(m):
    # 実装は入れていません、自分で入れてください
    
    #   m <= 1700　and m > 0 のとき、これがそのまま戻り値になる
    money = 610
    
    #   m > 1700以上か、適切な数値か
    if m > 1700 and m >= 1:
        
        #   追加料金のための計算
        money = (m - 1700) // 315 +1 
        
        
        #   これがないと(m - 1700) % 315 == 0　のときは料金が高くなる対策
        if (m - 1700) % 315 == 0 and money > 1  :
            money = money - 1 
            
        
        #金額もとめる
        money = money * 80 + 610
        
        
    elif m < 1:
        
        money = None
        
        
    return money
        
    
    #pass

if __name__ == "__main__":
    from argparse import ArgumentParser
    import sys

    parser = ArgumentParser(description="引数に金額を渡すとタクシー料金を計算します")
    parser.add_argument("distance", help="走行距離(メートル)", type=int)

    args = parser.parse_args()
    d = args.distance
    a = calc_account(d)
    if a == None:
        print("不正な数値です、1以上の整数値を渡してください", file=sys.stderr)
        sys.exit(1)
    print(f"走行距離 {args.distance}m => 金額は {calc_account(args.distance)}円です。")


