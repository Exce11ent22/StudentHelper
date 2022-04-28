package cs.vsu.ru;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@RestController
public class QuestionManager {

    public static void main(String[] args) {
        SpringApplication.run(QuestionManager.class, args);
    }

    @GetMapping("/question")
    public void showQuestion() {
        //TODO: get and show
    }

    public void inputAnswer() {
        //TODO: send an answer with file
    }

    public void showAnswers() {
        //TODO: get and show answers, if any
    }

}
