package net.codewyre.strawberry_py.codegen.lambdas;

import com.samskivert.mustache.Mustache;
import com.samskivert.mustache.Template;
import org.openapitools.codegen.*;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
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
public class MapDataTypeLambda implements Mustache.Lambda {
  private CodegenConfig generator = null;

  public MapDataTypeLambda() {

  }

  public MapDataTypeLambda generator(final CodegenConfig generator) {
    this.generator = generator;
    return this;
  }

  @Override
  public void execute(Template.Fragment fragment, Writer writer) throws IOException {
    String text = mapType(fragment.execute());
    if (generator != null && generator.reservedWords().contains(text)) {
      text = generator.escapeReservedWord(text);
    }
    writer.write(text);

  }

  private String mapType(String name) {
    HashMap<String, String> typeMap = new HashMap<>();
    typeMap.put("String", "str");
    typeMap.put("Long", "int");
    typeMap.put("List", "list");
    typeMap.put("Integer", "int");
    typeMap.put("Boolean", "bool");
    typeMap.put("File", "'file'");
    typeMap.put("DateTime", "datetime");
    typeMap.put("Date", "date");
    typeMap.put("Map", "dict");

    if (typeMap.containsKey(name)) {
      return typeMap.get(name);
    }

    return name;
  }

}