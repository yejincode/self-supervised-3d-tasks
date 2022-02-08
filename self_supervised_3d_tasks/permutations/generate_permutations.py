from pathlib import Path
import numpy as np


if __name__ == "__main__":
    perms = []

    for i in range(100):
        pp = np.random.permutation(27) #0에서 26까지를 무작위로 섞은 배열을 pp에 담음 ex) [26 4 7 0 ... 23]
        # print(pp)

        for ref in perms: #perms 안 요소의 수만큼 반복
            if (pp==ref).all(): #true라면.. 
                print("REGENERATE!!!!")

        perms.append(pp) #perms 배열에 위에서 만들어진 pp 배열을 붙인다. 

    perms = np.stack(perms) #perms 배열을 쌓음 (1차원,,,2차원,,,)

    permutation_path = str( #부모 디렉토리 경로 가져오기
        Path(__file__).parent / "permutations3d_100_27.npy"
    )

    print(permutation_path)

    with open(permutation_path, 'wb') as f: #쓰기모드 
        np.save(f, perms) #perms 배열 저장
