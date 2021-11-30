package fig.basic;

import java.lang.annotation.*;

@Retention(RetentionPolicy.RUNTIME)
//@Target(ElementType.FIELD)
//@Target(ElementType.METHOD)
public @interface Option {
  String name() default "";
  String gloss() default "";
  boolean required() default false;

  // Conditionally required option, e.g.
  //   - "main.operation": required only when main.operation specified
  //   - "main.operation=op1": required only when main.operation takes on value op1
  //   - "operation=op1": the group of the option is used
  String condReq() default "";
}

