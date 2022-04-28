package cs.vsu.ru;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@RestController
public class ChangeManager {

    public static void main(String[] args) {
        SpringApplication.run(ChangeManager.class, args);
    }

    @GetMapping("/change")
    public void changeProfile() {
        //TODO: change user info
    }

}
