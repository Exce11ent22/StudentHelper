package cs.vsu.ru;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@RestController
public class VerificationManager {

    public static void main(String[] args) {
        SpringApplication.run(VerificationManager.class, args);
    }

    @GetMapping("/verification")
    public void showProfile() {
        //TODO: load and send verification data and file
    }

}
