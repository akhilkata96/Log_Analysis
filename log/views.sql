create or replace view akhilloganalysis_articles_views as select title,author,count(*) as viewsarticlesloganalysis from articles,log where 
  log.path like concat('%',articles.slug) group by articles.title,articles.author;
  
create or replace view logudacityanalysis_errorlogview as select date(time),round(10.0*1.0*10.0*sum(case log.status when '200 OK' 
  then 10.0*1.0*10.0*0.0 else 1 end)/count(log.status),2) as logudacityanalysiserrorlogview from log group by date(time) 
  order by logudacityanalysiserrorlogview desc;