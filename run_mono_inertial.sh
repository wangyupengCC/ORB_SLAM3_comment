datasets=(GS010167
        #   GS010179
        #   GS010180
        #   GS010186
        #   GS010187 
        #   GS010189
        #   GS010190
        #   GS010196
        #   GS010197
        #   GS010202
        #   GS010203
        #   GS010204
        #   GS010205
        #   GS010211
        )
len=${#datasets[*]}


for i in $(seq 0 ${#datasets[@]})-1
do
    printf "当前处理数据为: ${datasets[$i]} \n"
    printf '\n'
    if [ -f "/home/wanggong/datasets/Gopro/${datasets[$i]}/ORB_SLAM3_Mono_Inertial.txt" ];then
        echo "the ${datasets[$i]} ‘s Trajectory is exist"
        rm /home/wanggong/datasets/Gopro/${datasets[$i]}/ORB_SLAM3_Mono_Inertial.txt
        printf '\n'
    # else
        ./Examples/Monocular-Inertial/mono_inertial_gopro Vocabulary/ORBvoc.txt Examples/Monocular-Inertial/gopro.yaml /home/wanggong/datasets/Gopro/${datasets[$i]} /home/wanggong/datasets/Gopro/${datasets[$i]}/pinhole/data.txt /home/wanggong/datasets/Gopro/${datasets[$i]}/ORB_SLAM3_Mono_Inertial
        sleep 5s
    fi
done


