/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package readcluster;
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
public class Readcluster {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Readcluster read=new Readcluster();
        for(int i=1;i<9;i++){
            read.cluster("cluster"+i);
        }
//        read.cluster("cluster1");
//        read.cluster("cluster2");
    }
    
    public void cluster(String filename){
        String sql= "SELECT IsJobFintech FROM "+filename;
         try {
            Class.forName("org.relique.jdbc.csv.CsvDriver");
            Connection connection = DriverManager.getConnection("jdbc:relique:csv:/Users/cestdrama/Desktop/");
            Statement statement = connection.createStatement();
            ResultSet results = statement.executeQuery(sql);
            ResultSetMetaData data = results.getMetaData();
             // get titles
            
            int columnCount = data.getColumnCount();
//           // String[] titles = new String[columnCount];
//            for (int i = 1; i <= columnCount; i++) {
//                String title = data.getColumnName(i);
//               // titles[i-1] = title;
//            }

           int notfin=0;
           int count=0;
           boolean isfincluster=true;
            while (results.next()) {
               
                for (int i = 1; i <=columnCount ; i++) {
                    String title=data.getColumnName(i);
                    String value = results.getString(i);
                    if(title.equals("IsJobFintech")){
                      if(!value.equals("1")){
                          notfin++;
                           count++;
                          isfincluster=false;
                      }
                      else  count++;
                    }
                    
                }
            }
            if (isfincluster==true) System.out.println(filename+" is fincluster"+" "+"total amount:"+count);
            else System.out.println(filename+" is not fincluster"+" "+"total amount:"+count+" "+"not amount"+notfin);
           
            results.close();
            statement.close();
            connection.close();
         }catch (Exception e) {
            e.printStackTrace();
        }
    }
    
}
