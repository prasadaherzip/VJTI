import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;

public class JdbcInsertExample {

    public static void main(String[] args) {

        String url = "jdbc:mysql://localhost:3306/college";
        String username = "root";
        String password = "root";

        try {
            Class.forName("com.mysql.cj.jdbc.Driver");

            Connection con = DriverManager.getConnection(url, username, password);
            System.out.println("Connected to database successfully!");

            String sql = "INSERT INTO student (id, name, marks) VALUES (?, ?, ?)";
            PreparedStatement pst = con.prepareStatement(sql);

            pst.setInt(1, 1);
            pst.setString(2, "Rahul");
            pst.setInt(3, 85);

            int rows = pst.executeUpdate();

            if (rows > 0)
                System.out.println("Data inserted successfully!");

            pst.close();
            con.close();

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}