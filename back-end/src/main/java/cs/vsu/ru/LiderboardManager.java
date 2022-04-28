package cs.vsu.ru;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@RestController
public class LiderboardManager {

    public static void main(String[] args) {
        SpringApplication.run(LiderboardManager.class, args);
    }

    @GetMapping("/liderboard")
    public void showTable() {
        //TODO: get and show some entries
    }

}
