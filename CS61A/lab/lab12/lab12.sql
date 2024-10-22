CREATE TABLE finals AS
  SELECT "RSF" AS hall, "61A" as course UNION
  SELECT "Wheeler"    , "61A"           UNION
  SELECT "Pimentel"   , "61A"           UNION
  SELECT "Li Ka Shing", "61A"           UNION
  SELECT "Stanley"    , "61A"           UNION
  SELECT "RSF"        , "61B"           UNION
  SELECT "Wheeler"    , "61B"           UNION
  SELECT "Morgan"     , "61B"           UNION
  SELECT "Wheeler"    , "61C"           UNION
  SELECT "Pimentel"   , "61C"           UNION
  SELECT "Soda 310"   , "61C"           UNION
  SELECT "Soda 306"   , "10"            UNION
  SELECT "RSF"        , "70";

CREATE TABLE sizes AS
  SELECT "RSF" AS room, 900 as seats    UNION
  SELECT "Wheeler"    , 700             UNION
  SELECT "Pimentel"   , 500             UNION
  SELECT "Li Ka Shing", 300             UNION
  SELECT "Stanley"    , 300             UNION
  SELECT "Morgan"     , 100             UNION
  SELECT "Soda 306"   , 80              UNION
  SELECT "Soda 310"   , 40              UNION
  SELECT "Soda 320"   , 30;

CREATE TABLE big AS
  SELECT course AS course
  FROM finals 
  JOIN sizes  ON hall=room  --这里是两个table 拼接在一起
  GROUP BY course
  HAVING SUM(seats)>=1000
  ;

CREATE TABLE remaining AS
  SELECT course,SUM(seats)-MAX(seats) AS remaining --前面在from中存在名字 无需取别名
  FROM finals,sizes
  --JOIN sizes ON hall = room
  --alternative way
  WHERE hall=room
  GROUP BY course
  ;

CREATE TABLE sharing AS
  SELECT a.course , COUNT(DISTINCT a.hall) AS sharing
  --要用distinct 是因为一门课程内部也会有重复使用的现象 但是这个就只算一次了
  FROM finals AS a, finals AS b
  WHERE a.hall=b.hall AND a.course <> b.course 
  -- 找出所有与a课程use the same room btw not the same course
  GROUP BY a.course ;
  --course 没有出现 只有course会不清楚是找a中的还是找b中的course

CREATE TABLE pairs AS
  SELECT a.room || " and " || b.room|| " together have " || (a.seats+b.seats) || " seats" AS rooms
  --这里运算不加括号无法输出了 为啥
  --会先运算+法 而不会去管||了 就不会存在与其他字符串连接的问题 
  --括号运算后得到的是string 结果 就会来连接了
  FROM sizes AS a,sizes AS b
  --有一个bug是 因为某个hall会同时出现多次 所以会有多次组合 输出重复结果
  --只用一个table就够啦！
  WHERE a.room<b.room AND (a.seats+b.seats)>=1000
  ORDER BY (a.seats+b.seats) DESC
  ;

