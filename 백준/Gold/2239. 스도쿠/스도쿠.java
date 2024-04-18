import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.List;

public class Main {
    private static int[][] arr;
    private static int[][] result;
    private static List<Point> que;
    private static int L;
    private static boolean endFlag;

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

        arr = new int[9][9];

        que = new LinkedList<>();

        for (int i = 0; i < 9; i++) {
            String line = input.readLine();

            for (int j = 0; j < 9; j++) {
                int num = Character.getNumericValue(line.charAt(j));

                arr[i][j] = num;

                if (num == 0) {
                    que.add(new Point(i, j));
                }
            }
        }

        L = que.size();

        result = new int[9][9];

        endFlag = false;

        backTracking(0);

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                sb.append(result[i][j]);
            }
            if (i != 8) {
                sb.append("\n");
            }
        }

        System.out.println(sb);
    }

    static void backTracking(int idx) {
        if (idx == L) {
            for (int i = 0; i < 9; i++) {
                for (int j = 0; j < 9; j++) {
                    result[i][j] = arr[i][j];
                }
            }
            endFlag = true;
            return;
        }

        if (endFlag) {
            return;
        }

        Point now = que.get(idx);

        for (int val = 1; val < 10; val++) {
            if (checkRow(now.x, val) && checkColumn(now.y, val) && checkSquare(now.x / 3, now.y / 3, val)) {
                arr[now.x][now.y] = val;
                backTracking(idx + 1);

                if (endFlag) {
                    break;
                }

                arr[now.x][now.y] = 0;
            }
        }
    }

    static boolean checkRow() {
        for (int i = 0; i < 9; i++) {
            int[] checkList = new int[9];

            for (int j = 0; j < 9; j++) {
                int n = arr[i][j];

                if (checkList[n - 1] == 0) {
                    checkList[n - 1] += 1;
                } else {
                    return false;
                }
            }
        }
        return true;
    }

    static boolean checkRow(int r, int value) {
        for (int c = 0; c < 9; c++) {
            if (arr[r][c] == value) {
                return false;
            }
        }
        return true;
    }

    static boolean checkColumn() {
        for (int i = 0; i < 9; i++) {
            int[] checkList = new int[9];

            for (int j = 0; j < 9; j++) {
                int n = arr[j][i];

                if (checkList[n - 1] == 0) {
                    checkList[n - 1] += 1;
                } else {
                    return false;
                }
            }
        }
        return true;
    }

    static boolean checkColumn(int c, int value) {
        for (int r = 0; r < 9; r++) {
            if (arr[r][c] == value) {
                return false;
            }
        }
        return true;
    }
    static boolean checkSquare() {
        for (int sumRow = 0; sumRow < 3; sumRow++) {
            for (int sumCol = 0; sumCol < 3; sumCol++) {
                int[] checkList = new int[9];

                for (int i = sumRow * 3; i < (sumRow + 1) * 3; i++) {
                    for (int j = sumCol * 3; j < (sumCol + 1) * 3; j++) {
                        int n = arr[j][i];

                        if (checkList[n - 1] == 0) {
                            checkList[n - 1] += 1;
                        } else {
                            return false;
                        }
                    }
                }
            }
        }
        return true;
    }

    static boolean checkSquare(int r, int c, int value) {
        for (int i = r * 3; i < (r + 1) * 3; i++) {
            for (int j = c * 3; j < (c + 1) * 3; j++) {
                if (arr[i][j] == value) {
                    return false;
                }
            }
        }
        return true;
    }
}