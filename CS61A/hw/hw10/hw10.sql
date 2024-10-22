CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT a.child AS name
  FROM parents AS a, dogs AS b --如果要从两个表格中得到数据 那么需要两个object 来交叉对比
  WHERE a.parent=b.name --只会筛选出b中有parent name的row 
  ORDER BY b.height DESC; --在那个where之后 相当于a表有append的了与b中name相同的数据


-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT a.name AS dogname, b.size AS sizename
  FROM dogs AS a, sizes AS b
  WHERE a.height > b.min AND a.height <= b.max; --我不确定的是 这里是否指的是同一行
  -- 有个发现 其实只要用到其中一个条件了 那么就会限定在一个row中 那么剩下所有条件都是使用这一row中的


-- Filling out this helper table is optional
CREATE TABLE siblings AS --has the same granddad
  SELECT a.child AS name1, c.child AS name2
  FROM parents AS a
  JOIN
   parents AS b ON a.parent=b.child
   JOIN --不用join也可以 但是要学学join
    parents AS c ON c.parent=b.child
  WHERE a.child <> c.child; --a.child and b.parent gandson/granddad

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT "The two siblings, " || a.name1 || " and "|| a.name2 || ", have the same size: " || b.sizename
  FROM siblings AS a, size_of_dogs AS b, size_of_dogs AS c
  WHERE a.name1=b.dogname AND a.name2=c.dogname AND b.sizename=c.sizename
  AND a.name1<a.name2 --这一下使得两项一样的 有了区分 ！
  ;


-- Height range for each fur type where all of the heights differ by no more than 30% from the average height
CREATE TABLE low_variance AS
  SELECT fur AS nametype , MAX(height)-MIN(height) AS range 
  FROM dogs 
  GROUP BY fur --相同fur的会被放在一组
  HAVING MIN(height)>=AVG(height)*0.7 AND MAX(height)<=AVG(height)*1.3
  --having 中manipulate必须要在group by中提出 height不在fur中 只能使用聚合函数得到数据 
  --average 直接就是整个column 的平均
  --为什么不能用heigh而是直接用min/max 
  --
  ;

