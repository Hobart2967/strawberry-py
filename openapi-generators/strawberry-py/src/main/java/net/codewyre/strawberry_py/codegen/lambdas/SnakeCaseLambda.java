package net.codewyre.strawberry_py.codegen.lambdas;

import com.samskivert.mustache.Mustache;
import com.samskivert.mustache.Template;
import org.openapitools.codegen.*;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.*;
import java.io.IOException;
import java.io.Writer;

/**
 * Converts text in a fragment to lowercase.
 *
 * Register:
 * 
 * <pre>
 * additionalProperties.put("lowercase", new LowercaseLambda());
 * </pre>
 *
 * Use:
 * 
 * <pre>
 * {{#lowercase}}{{httpMethod}}{{/lowercase}}
 * </pre>
 */
public class SnakeCaseLambda implements Mustache.Lambda {
  private CodegenConfig generator = null;

  public SnakeCaseLambda() {

  }

  public SnakeCaseLambda generator(final CodegenConfig generator) {
    this.generator = generator;
    return this;
  }

  @Override
  public void execute(Template.Fragment fragment, Writer writer) throws IOException {
    String text = upperUnderscoreWithAcronyms(fragment.execute()).toLowerCase();
    if (generator != null && generator.reservedWords().contains(text)) {
      text = generator.escapeReservedWord(text);
    }
    writer.write(text);
  }

  private String upperUnderscoreWithAcronyms(String name) {
    return SnakeCaseLambda.toSnakeCase(name);
  }

  private static String toSnakeCase(String name) {
    if (name.contains(".")) {
      String[] segments = name.split("\\.");
      for (int i = 0; i < segments.length; i++) {
        segments[i] = SnakeCaseLambda.toSnakeCase(segments[i]);
      }

      return String.join(".", segments);
    }

    StringBuffer result = new StringBuffer();
    boolean begin = true;
    boolean lastUppercase = false;
    for (int i = 0; i < name.length(); i++) {
      char ch = name.charAt(i);
      if (Character.isUpperCase(ch)) {
        // is start?
        if (begin) {
          result.append(ch);
        } else {
          if (lastUppercase) {
            // test if end of acronym
            if (i + 1 < name.length()) {
              char next = name.charAt(i + 1);
              if (Character.isUpperCase(next)) {
                // acronym continues
                result.append(ch);
              } else {
                // end of acronym
                result.append('_').append(ch);
              }
            } else {
              // acronym continues
              result.append(ch);
            }
          } else {
            // last was lowercase, insert _
            result.append('_').append(ch);
          }
        }
        lastUppercase = true;
      } else {
        result.append(Character.toUpperCase(ch));
        lastUppercase = false;
      }
      begin = false;
    }
    return result.toString();
  }
}