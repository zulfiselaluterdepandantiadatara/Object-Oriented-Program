// Student.java
public class Student {
    private String name;
    private String id;
    private char grade;
    
    public Student(String name, String id, char grade) {
        this.name = name;
        this.id = id;
        this.grade = grade;
    }
    
    // Getter methods
    public String getName() { return name; }
    public String getId() { return id; }
    public char getGrade() { return grade; }
}
