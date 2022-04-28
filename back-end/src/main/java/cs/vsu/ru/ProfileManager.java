package cs.vsu.ru;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@RestController
public class ProfileManager {

    public static void main(String[] args) {
        SpringApplication.run(ProfileManager.class, args);
    }

    @GetMapping("/profile")
    public void showProfile() {
        //TODO: get and show user info
    }

}
