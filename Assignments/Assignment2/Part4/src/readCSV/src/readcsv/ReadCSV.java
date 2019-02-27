/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package readcsv;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.Statement;
//import java.util.ArrayList;
import java.util.*;
import com.csvreader.CsvWriter;
import java.io.*;
import java.nio.charset.Charset;

/**
 *
 * @author cestdrama
 */
public class ReadCSV {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        ReadCSV read=new ReadCSV();
        read.readcomjob("job-company");      
        read.readfintechjob("job-company");
    }
    
    public void readcomjob(String filename){
//        String filename="job-company";
        String sql= "SELECT * FROM "+filename;
         try {
            Class.forName("org.relique.jdbc.csv.CsvDriver");
            Connection connection = DriverManager.getConnection("jdbc:relique:csv:/Users/cestdrama/Desktop/");
            Statement statement = connection.createStatement();
            ResultSet results = statement.executeQuery(sql);
            ResultSetMetaData data = results.getMetaData();
             // get titles
            int jcount=0;
            int columnCount = data.getColumnCount();
           // String[] titles = new String[columnCount];
            for (int i = 1; i <= columnCount; i++) {
                String title = data.getColumnName(i);
               // titles[i-1] = title;
            }

            List<String[]> result = new ArrayList<>();
            Map<String,Integer> comname=new HashMap();
           
            while (results.next()) {
                int count;
                for (int i = 1; i <=columnCount ; i++) {
                    String title=data.getColumnName(i);
                    String value = results.getString(i);
                    if(title.equals("Institution")){
                       if(!comname.containsKey(value)){
                        /// count=1;                         
                         comname.put(value,1);
                       }
                       else comname.put(value,comname.get(value)+1);                       
                    }
                    
                }
            }
            int count=0;
            Set<Map.Entry<String,Integer>> mapSet = comname.entrySet();
            for(Map.Entry<String,Integer> mapEntry : mapSet){
            System.out.println(mapEntry.getKey()+":"+mapEntry.getValue());
            count=count+mapEntry.getValue();
            }
//            ReadCSV in=new ReadCSV();
            write(comname,"company.csv");
            System.out.println("total:"+count);
            results.close();
            statement.close();
            connection.close();
         }catch (Exception e) {
            e.printStackTrace();
        }
        
    }
    
    public void readfintechjob(String filename){
//        String sql= "SELECT Institution,IsFintechJob FROM"+filename;
         String sql= "SELECT Institution,IsFintechJob FROM "+filename;
         try {
            Class.forName("org.relique.jdbc.csv.CsvDriver");
            Connection connection = DriverManager.getConnection("jdbc:relique:csv:/Users/cestdrama/Desktop/");
            Statement statement = connection.createStatement();
            ResultSet results = statement.executeQuery(sql);
            ResultSetMetaData data = results.getMetaData();
            
            int columnCount = data.getColumnCount();
           
            String[] titles = new String[columnCount];
            for (int i = 1; i <= columnCount; i++) {
                String title = data.getColumnName(i);
                titles[i-1] = title;
            }
                       
             // get results 
            List<String[]> result = new ArrayList<>();
            List<String> com=new ArrayList<>();
            List<String> flag=new ArrayList<>();
            while (results.next()) {
                String[] row = new String[columnCount];
                for (int i = 1; i <= columnCount; i++) {
                    String value = results.getString(i);
                    row[i-1] = value;
                }
                result.add(row);
            }
            
           //单独存储每一列的数据
            for(String[] arr:result){
                for(int j=0;j<arr.length;j++){
                    if(j%2==0) com.add(arr[j]);
                    else flag.add(arr[j]);
                }
            }
            Map<String,Integer> finmap=new HashMap();
            Map<String,Integer> notmap=new HashMap();
            for(int k=0;k<com.size();k++){
                String key=com.get(k);
                Integer value=Integer.parseInt(flag.get(k));
                if(value==1){
                    if(!finmap.containsKey(key))
                        finmap.put(key,1);
                    else finmap.put(key,finmap.get(key)+1);
                }
                else if(value==0){
                     if(!notmap.containsKey(key))
                        notmap.put(key,1);
                    else notmap.put(key,notmap.get(key)+1);
                }
            }
            
            int count=0;
            int count2=0;
            String[] c1=new String[finmap.size()];
            String[] c2=new String[finmap.size()];
            String[] c3=new String[finmap.size()];
            System.out.println("***************************");
            Set<Map.Entry<String,Integer>> mapSet = finmap.entrySet();
            int j=0;
            for(Map.Entry<String,Integer> mapEntry : mapSet){
            System.out.println(mapEntry.getKey()+":"+mapEntry.getValue());
            c1[j]=mapEntry.getKey();
            c2[j]=String.valueOf(mapEntry.getValue());
//            System.out.println("~~"+c1[j]+" "+c2[j]+"~~");
            j++;
            count=count+mapEntry.getValue();
            }
            System.out.println("total:"+count);
            System.out.println("***************************");
            int h=0;
            Set<Map.Entry<String,Integer>> Set = notmap.entrySet();
            for(Map.Entry<String,Integer> Entry : Set){
            System.out.println(Entry.getKey()+":"+Entry.getValue());
            c3[h]=String.valueOf(Entry.getValue());
            h++;
            count2=count2+Entry.getValue();
            }
            System.out.println("total not:"+count2);
            
            
            
//           
            String[] headers={"Institution","fin-job","not-finjob"};
            System.out.println("***************************");
             List<String[]> content = new ArrayList<>();
            for(int n=0;n<c1.length;n++){  
               int m=0;
               String[] newrow=new String[3];
               while(m<3){
                  newrow[m]=c1[n];
                  newrow[m+1]=c2[n];
                  newrow[m+2]=c3[n];  
                  System.out.println(newrow[m]+" "+newrow[m+1]+" "+newrow[m+2]);
                  System.out.println(c1[n]+" "+c2[n]+" "+c3[n]);
                  m=m+3;
                  
               }
               //csvWriter.writeRecord(newrow);
               content.add(newrow);
               write(headers,content,"finORnot.csv");
            }
            
         }catch (Exception e) {
            e.printStackTrace();
        }
    }
    
    public void write(Map<String,Integer> map,String outname){
        String filePath = "/Users/cestdrama/Desktop/6105data/ass2/"+outname;

        try {
            // 创建CSV写对象
            CsvWriter csvWriter = new CsvWriter(filePath,',', Charset.forName("utf-8"));
            //CsvWriter csvWriter = new CsvWriter(filePath);

            // 写表头
            String[] headers = {"Company","Amount"};
            csvWriter.writeRecord(headers);
            Set<Map.Entry<String,Integer>> mapSet = map.entrySet();
            for(Map.Entry<String,Integer> mapEntry : mapSet){
                String[] content = {mapEntry.getKey(), String.valueOf(mapEntry.getValue())};
                csvWriter.writeRecord(content);
            }
            csvWriter.close();

        } catch (IOException e) {
            e.printStackTrace();
        }
        
    }
    
    public void write(String[] headers,List<String[]> result,String outname){
        String filePath = "/Users/cestdrama/Desktop/6105data/ass2/"+outname;

        try {
            // 创建CSV写对象
            CsvWriter csvWriter = new CsvWriter(filePath,',', Charset.forName("utf-8"));
            //CsvWriter csvWriter = new CsvWriter(filePath);

            // 写表头
            csvWriter.writeRecord(headers);
            for(String[] content:result){
                csvWriter.writeRecord(content);
            }

            csvWriter.close();

        } catch (IOException e) {
            e.printStackTrace();
        }
        
        
    }
    
}
