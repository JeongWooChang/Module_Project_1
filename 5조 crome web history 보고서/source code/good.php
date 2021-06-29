<?php
   $conn = mysqli_connect("db", "devuser", "devpass" , "test_db");
   $sql = "SELECT contents, time FROM goodhistory";
   $result = mysqli_query($conn, $sql);
   if (mysqli_num_rows($result) > 0) {
   while($row = mysqli_fetch_assoc($result)) {
   echo "학습관련 웹히스토리: " . $row["contents"]. " 접속시간:" . $row["time"]. "<br>";
   }
   }else{
   echo "테이블에 데이터가 없습니다.";
   }
   echo "Total: ", mysqli_num_rows($result);
   mysqli_close($conn); // 디비 접속 닫기
?>