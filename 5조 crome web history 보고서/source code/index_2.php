<?php 
    $conn = mysqli_connect("db", "devuser", "devpass" , "test_db");

    $goodsql = "SELECT contents, time FROM goodhistory";
    $badsql = "SELECT contents, time FROM badhistory";

    $good_cnt = mysqli_num_rows(mysqli_query($conn, $goodsql));
    $bad_cnt = mysqli_num_rows(mysqli_query($conn, $badsql));
    $total_cnt = $good_cnt + $bad_cnt;

    $result = (int)(($good_cnt / $total_cnt) * 100);

    echo "전체학습률 : $result%  <br>";
    echo "학습태도 : ";
    if($result >= 80){
        echo "우수";
    }
    elseif($result >= 60){
        echo "보통";
    }
    else{
        echo "나쁨";
    }
    echo "<br><br>";
    echo "Total Good History Count :  $good_cnt  <br>";
    echo "Total Bad History Count :  $bad_cnt <br>";

    mysqli_close($conn); // 디비 접속 닫기
?>


