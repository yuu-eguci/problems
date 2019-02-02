import java.util.Arrays;
import java.util.Scanner;

public class Main {
	
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();
        
        //�P�̏ꍇ�͌v�Z���Ȃ�
        if (N == 1) {
        	System.out.println(1);
        	return;
        }
        
        //�e�}�X�̈ړ����������O�Ɍv�Z�@O(N)
        int[] map = new int[N+1];
        for (int i = 1; i <= N; i++) {
        	map[i] = Integer.bitCount(i);
        }
        
        //�e�}�X�ւ̍ŒZ�����̔z����쐬
        int[] dp = new int[N+1];
        Arrays.fill(dp, Integer.MAX_VALUE-500);
        dp[1] = map[1];
        
        
        
        //�ύX����ӏ����Ȃ��Ȃ�����I�� �ň���O(N^2) ������ N=10^4 �Ȃ̂�N^2=10^8��java�Ȃ�Ԃɍ���
        boolean changed = true;
        while(changed) {
        	changed = false;
        	//�P�}�X�ڂ���ŒZ�������v�Z���Ă���
        	for (int i = 1; i <=N; i++) {
        		//���̃}�X����߂����ق����}�X�������Ȃ��ꍇ�͍X�V�����ꂪ�ŒZ����
        		if (i-map[i] > 0 && dp[i-map[i]] > dp[i]+1) {
        			dp[i-map[i]] = dp[i]+1;
        			changed = true;
        		}
        		
        		//���̃}�X����i�񂾂ق����}�X�������Ȃ��ꍇ�͍X�V�����ꂪ�ŒZ����
        		if (i+map[i] <= N && dp[i+map[i]] > dp[i]+1) {
        			dp[i+map[i]] = dp[i]+1;
        			changed = true;
        		}
        	}
        }
        
        //N�}�X�ڂ������l�̂܂܂������瓞�B�s�\�Ƃ���-1���o��
        System.out.println(dp[N] == Integer.MAX_VALUE-500 ? -1 : dp[N]);
    }
}


