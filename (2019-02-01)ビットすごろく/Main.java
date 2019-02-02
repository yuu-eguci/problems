import java.util.Arrays;
import java.util.Scanner;

public class Main {
	
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();
        
        //１の場合は計算しない
        if (N == 1) {
        	System.out.println(1);
        	return;
        }
        
        //各マスの移動距離を事前に計算　O(N)
        int[] map = new int[N+1];
        for (int i = 1; i <= N; i++) {
        	map[i] = Integer.bitCount(i);
        }
        
        //各マスへの最短距離の配列を作成
        int[] dp = new int[N+1];
        Arrays.fill(dp, Integer.MAX_VALUE-500);
        dp[1] = map[1];
        
        
        
        //変更する箇所がなくなったら終了 最悪がO(N^2) 制約より N=10^4 なのでN^2=10^8はjavaなら間に合う
        boolean changed = true;
        while(changed) {
        	changed = false;
        	//１マス目から最短距離を計算していく
        	for (int i = 1; i <=N; i++) {
        		//今のマスから戻ったほうがマス数が少ない場合は更新＜これが最短距離
        		if (i-map[i] > 0 && dp[i-map[i]] > dp[i]+1) {
        			dp[i-map[i]] = dp[i]+1;
        			changed = true;
        		}
        		
        		//今のマスから進んだほうがマス数が少ない場合は更新＜これが最短距離
        		if (i+map[i] <= N && dp[i+map[i]] > dp[i]+1) {
        			dp[i+map[i]] = dp[i]+1;
        			changed = true;
        		}
        	}
        }
        
        //Nマス目が初期値のままだったら到達不可能として-1を出力
        System.out.println(dp[N] == Integer.MAX_VALUE-500 ? -1 : dp[N]);
    }
}


