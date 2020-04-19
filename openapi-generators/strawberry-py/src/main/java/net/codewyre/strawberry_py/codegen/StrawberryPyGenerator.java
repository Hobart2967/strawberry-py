package net.codewyre.strawberry_py.codegen;

import org.apache.commons.lang3.StringUtils;
import org.openapitools.codegen.*;
import org.openapitools.codegen.templating.mustache.LowercaseLambda;

import io.swagger.models.properties.*;
import io.swagger.v3.oas.models.media.Schema;
import net.codewyre.strawberry_py.codegen.lambdas.MapDataTypeLambda;
import net.codewyre.strawberry_py.codegen.lambdas.SnakeCaseLambda;

import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.io.File;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class StrawberryPyGenerator extends DefaultCodegen implements CodegenConfig {
  private static final Logger LOGGER = LoggerFactory.getLogger(StrawberryPyGenerator.class);
  // source folder where to write the files
  protected String sourceFolder = "src";
  protected String apiVersion = "1.0.0";

  /**
   * Configures the type of generator.
   *
   * @return  the CodegenType for this generator
   * @see     org.openapitools.codegen.CodegenType
   */
  public CodegenType getTag() {
    return CodegenType.OTHER;
  }


  protected String packageName = "strawberry-codegen-project";

  /**
   * Configures a friendly name for the generator.  This will be used by the generator
   * to select the library with the -g flag.
   *
   * @return the friendly name for the generator
   */
  public String getName() {
    return "strawberry-py";
  }

  @Override
  public String toApiFilename(String name) {
      return underscore(toApiName(name));
  }

  @Override
  public String getTypeDeclaration(Schema schema) {
    return  super.getTypeDeclaration(schema);
  }

  @Override
  public String toVarName(String name) {
      // sanitize name
      name = sanitizeName(name); // FIXME: a parameter should not be assigned. Also declare the methods parameters as 'final'.

      // remove dollar sign
      name = name.replaceAll("$", "");

      // if it's all uppper case, convert to lower case
      if (name.matches("^[A-Z_]*$")) {
          name = name.toLowerCase();
      }

      // underscore the variable name
      // petId => pet_id
      name = underscore(name);

      // remove leading underscore
      name = name.replaceAll("^_*", "");

      // for reserved word or word starting with number, append _
      if (isReservedWord(name) || name.matches("^\\d.*")) {
          name = escapeReservedWord(name);
      }

      return name;
  }

  //@Override
  //public String toParamName(String name) {
  //    // don't do name =removeNonNameElementToCamelCase(name); // this breaks connexion, which does not modify param names before sending them
  //    if (reservedWords.contains(name)) {
  //        name = escapeReservedWord(name);
  //    }
  //    // Param name is already sanitized in swagger spec processing
  //    return toVarName(name);
  //}

  private static String dropDots(String str) {
    return str.replaceAll("\\.", "_");
  }

  @Override
  public String toModelFilename(String name) {
      // underscore the model file name
      // PhoneNumber => phone_number
      return underscore(dropDots(toModelName(name)));
  }

  @Override
  public String toApiName(String name) {
    return super.toApiName(name) + "Controller";
  }

  @Override
  public String toModelName(String name) {
      name = sanitizeName(name); // FIXME: a parameter should not be assigned. Also declare the methods parameters as 'final'.
      // remove dollar sign
      name = name.replaceAll("$", "");

      // model name cannot use reserved keyword, e.g. return
      if (isReservedWord(name)) {
          LOGGER.warn(name + " (reserved word) cannot be used as model name. Renamed to " + camelize("model_" + name));
          name = "model_" + name; // e.g. return => ModelReturn (after camelize)
      }

      // model name starts with number
      if (name.matches("^\\d.*")) {
          LOGGER.warn(name + " (model name starts with number) cannot be used as model name. Renamed to " + camelize("model_" + name));
          name = "model_" + name; // e.g. 200Response => Model200Response (after camelize)
      }

      if (!StringUtils.isEmpty(modelNamePrefix)) {
          name = modelNamePrefix + "_" + name;
      }

      if (!StringUtils.isEmpty(modelNameSuffix)) {
          name = name + "_" + modelNameSuffix;
      }

      // camelize the model name
      // phone_number => PhoneNumber
      return camelize(name);
  }

  public static String camelize(String word) {
    return camelize(word, false);
}

  public static String camelize(String word, boolean lowercaseFirstLetter) {
    // Replace all slashes with dots (package separator)
    String originalWord = word;
    LOGGER.trace("camelize start - " + originalWord);
    Pattern p = Pattern.compile("\\/(.?)");
    Matcher m = p.matcher(word);
    int i = 0;
    int MAX = 100;
    while (m.find()) {
        if (i > MAX) {
            LOGGER.error("camelize reached find limit - {} / {}", originalWord, word);
            break;
        }
        i++;
        word = m.replaceFirst("." + m.group(1)/*.toUpperCase()*/); // FIXME: a parameter should not be assigned. Also declare the methods parameters as 'final'.
        m = p.matcher(word);
    }
    i = 0;
    // case out dots
    String[] parts = word.split("\\.");
    StringBuilder f = new StringBuilder();
    for (String z : parts) {
        if (z.length() > 0) {
            f.append(Character.toUpperCase(z.charAt(0))).append(z.substring(1));
        }
    }
    word = f.toString();

    m = p.matcher(word);
    while (m.find()) {
        if (i > MAX) {
            LOGGER.error("camelize reached find limit - {} / {}", originalWord, word);
            break;
        }
        i++;
        word = m.replaceFirst("" + Character.toUpperCase(m.group(1).charAt(0)) + m.group(1).substring(1)/*.toUpperCase()*/);
        m = p.matcher(word);
    }
    i = 0;
    // Uppercase the class name.
    p = Pattern.compile("(\\.?)(\\w)([^\\.]*)$");
    m = p.matcher(word);
    if (m.find()) {
        String rep = m.group(1) + m.group(2).toUpperCase() + m.group(3);
        rep = rep.replaceAll("\\$", "\\\\\\$");
        word = m.replaceAll(rep);
    }

    // Remove all underscores (underscore_case to camelCase)
    p = Pattern.compile("(_)(.)");
    m = p.matcher(word);
    while (m.find()) {
        if (i > MAX) {
            LOGGER.error("camelize reached find limit - {} / {}", originalWord, word);
            break;
        }
        i++;
        String original = m.group(2);
        String upperCase = original.toUpperCase();
        if (original.equals(upperCase)) {
            word = word.replaceFirst("_", "");
        } else {
            word = m.replaceFirst(upperCase);
        }
        m = p.matcher(word);
    }

    // Remove all hyphens (hyphen-case to camelCase)
    p = Pattern.compile("(-)(.)");
    m = p.matcher(word);
    i = 0;
    while (m.find()) {
        if (i > MAX) {
            LOGGER.error("camelize reached find limit - {} / {}", originalWord, word);
            break;
        }
        i++;
        word = m.replaceFirst(m.group(2).toUpperCase());
        m = p.matcher(word);
    }

    if (lowercaseFirstLetter && word.length() > 0) {
        word = word.substring(0, 1).toLowerCase() + word.substring(1);
    }
    LOGGER.trace("camelize end - {} (new: {})", originalWord, word);
    return word;
}

  @Override
  public String toOperationId(String operationId) {
      // throw exception if method name is empty (should not occur as an auto-generated method name will be used)
      if (StringUtils.isEmpty(operationId)) {
          throw new RuntimeException("Empty method name (operationId) not allowed");
      }

      // method name cannot use reserved keyword, e.g. return
      if (isReservedWord(operationId)) {
          LOGGER.warn(operationId + " (reserved word) cannot be used as method name. Renamed to " + underscore(sanitizeName("call_" + operationId)));
          operationId = "call_" + operationId;
      }

      return underscore(sanitizeName(operationId));
  }

  @Override
  public String getSchemaType(Schema schema) {
    return super.getSchemaType(schema);
  }

  @Override
  public void processOpts() {
      super.processOpts();
      // {{packageName}}
      if (additionalProperties.containsKey(CodegenConstants.PACKAGE_NAME)) {
          this.packageName = ((String) additionalProperties.get(CodegenConstants.PACKAGE_NAME));
      } else {
          additionalProperties.put(CodegenConstants.PACKAGE_NAME, packageName);
      }
  }

  /**
   * Provides an opportunity to inspect and modify operation data before the code is generated.
   */
  @SuppressWarnings("unchecked")
  @Override
  public Map<String, Object> postProcessOperationsWithModels(Map<String, Object> objs, List<Object> allModels) {

    // to try debugging your code generator:
    // set a break point on the next line.
    // then debug the JUnit test called LaunchGeneratorInDebugger

    Map<String, Object> results = super.postProcessOperationsWithModels(objs, allModels);

    Map<String, Object> ops = (Map<String, Object>)results.get("operations");
    ArrayList<CodegenOperation> opList = (ArrayList<CodegenOperation>)ops.get("operation");

    // iterate over the operation and perhaps modify something
    for(CodegenOperation co : opList){
      // example:
      // co.httpMethod = co.httpMethod.toLowerCase();
    }

    return results;
  }

  /**
   * Returns human-friendly help for the generator.  Provide the consumer with help
   * tips, parameters here
   *
   * @return A string value for the help message
   */
  public String getHelp() {
    return "Generates a strawberry-py client library.";
  }

  public StrawberryPyGenerator() {
    super();

    // set the output folder here
    outputFolder = "generated-code/strawberry-py";
    importMapping = new HashMap();
    importMapping.put("DateTime", "datetime");
    importMapping.put("Date", "datetime");
    /**
     * Models.  You can write model files using the modelTemplateFiles map.
     * if you want to create one template for file, you can do so here.
     * for multiple files for model, just put another entry in the `modelTemplateFiles` with
     * a different extension
     */
    modelTemplateFiles.put(
      "src/models/model.mustache", // the template to use
      ".py");       // the extension for each file to write

    /**
     * Api classes.  You can write classes for each Api file with the apiTemplateFiles map.
     * as with models, add multiple entries with different extensions for multiple files per
     * class
     */
    apiTemplateFiles.put(
      "src/controllers/controller.mustache",   // the template to use
      ".py");       // the extension for each file to write

    apiTemplateFiles.put(
        "src/controllers/controller_impl.mustache",   // the template to use
        "_impl.py");       // the extension for each file to write
  
    /**
     * Template Location.  This is the location which templates will be read from.  The generator
     * will use the resource stream to attempt to read the templates.
     */
    templateDir = "strawberry-py";

    /**
     * Api Package.  Optional, if needed, this can be used in templates
     */
    apiPackage = "src.controllers";

    /**
     * Model Package.  Optional, if needed, this can be used in templates
     */
    modelPackage = "src.models";

    /**
     * Reserved words.  Override this with reserved words specific to your language
     */
    reservedWords = new HashSet<String> (
      Arrays.asList()
    );

    addOption(CodegenConstants.PACKAGE_NAME,
      "C# package name (convention: Title.Case).",
      this.packageName);

    /**
     * Additional Properties.  These values can be passed to the templates and
     * are available in models, apis, and supporting files
     */
    additionalProperties.put("apiVersion", apiVersion);
    additionalProperties.put("lowercase", new LowercaseLambda());
    additionalProperties.put("snakecase", new SnakeCaseLambda());
    additionalProperties.put("maptype", new MapDataTypeLambda());
    /**
     * Supporting Files.  You can write single files for the generator with the
     * entire object tree available.  If the input file has a suffix of `.mustache
     * it will be processed by the template engine.  Otherwise, it will be copied
     */
    supportingFiles.add(new SupportingFile("src/main.mustache", "", "src/main.py"));
    supportingFiles.add(new SupportingFile(".openapi-generator-ignore.mustache", "", ".openapi-generator-ignore"));
    supportingFiles.add(new SupportingFile("serverless.mustache", "", "serverless.yml"));
    supportingFiles.add(new SupportingFile("package.mustache", "", "package.json"));
    supportingFiles.add(new SupportingFile("src/__init__.mustache", "", "src/__init__.py"));
    supportingFiles.add(new SupportingFile("src/models/__init__.mustache", "", "src/models/__init__.py"));
    supportingFiles.add(new SupportingFile("src/controllers/__init__.mustache", "", "src/controllers/__init__.py"));

    /**
     * Language Specific Primitives.  These types will not trigger imports by
     * the client generator
     */
    languageSpecificPrimitives = new HashSet<String>(
      Arrays.asList(
        "string",      // replace these with your types
        "file",
        "integer",
        "list",
        "array",
        "List",
        "Array",
        "Map",
        "map")
    );
  }


   /**
     * Return the default value of the property
     *
     * @param p Swagger property object
     * @return string presentation of the default value of the property
     */
    @Override
    public String toDefaultValue(Schema schema) {
      if (schema.getDefault() != null) {
        if (schema.getType() == "boolean") {
          return camelize(schema.getDefault().toString());
        }
        return schema.getDefault().toString();
      }

      return "None"; //getPropertyDefaultValue(schema);
    }

  public static String underscore(String word) {
    String firstPattern = "([A-Z]+)([A-Z][a-z])";
    String secondPattern = "([a-z\\d])([A-Z])";
    String replacementPattern = "$1_$2";
    // Replace package separator with slash.
    word = word.replaceAll("\\.", "/"); // FIXME: a parameter should not be assigned. Also declare the methods parameters as 'final'.
    // Replace $ with two underscores for inner classes.
    word = word.replaceAll("\\$", "__");
    // Replace capital letter with _ plus lowercase letter.
    word = word.replaceAll(firstPattern, replacementPattern);
    word = word.replaceAll(secondPattern, replacementPattern);
    word = word.replace('-', '_');
    // replace space with underscore
    word = word.replace(' ', '_');
    word = word.toLowerCase();
    return word;
}

  /**
   * Escapes a reserved word as defined in the `reservedWords` array. Handle escaping
   * those terms here.  This logic is only called if a variable matches the reserved words
   *
   * @return the escaped term
   */
  @Override
  public String escapeReservedWord(String name) {
    return "_" + name;  // add an underscore to the name
  }

  /**
   * Location to write model files.  You can use the modelPackage() as defined when the class is
   * instantiated
   */
  public String modelFileFolder() {
    return outputFolder + "/" + sourceFolder + "/models";
  }

  /**
   * Location to write api files.  You can use the apiPackage() as defined when the class is
   * instantiated
   */
  @Override
  public String apiFileFolder() {
    return outputFolder + "/" + sourceFolder + "/controllers";
  }

  /**
   * override with any special text escaping logic to handle unsafe
   * characters so as to avoid code injection
   *
   * @param input String to be cleaned up
   * @return string with unsafe characters removed or escaped
   */
  @Override
  public String escapeUnsafeCharacters(String input) {
    //TODO: check that this logic is safe to escape unsafe characters to avoid code injection
    return input;
  }

  /**
   * Escape single and/or double quote to avoid code injection
   *
   * @param input String to be cleaned up
   * @return string with quotation mark removed or escaped
   */
  public String escapeQuotationMark(String input) {
    //TODO: check that this logic is safe to escape quotation mark to avoid code injection
    return input.replace("\"", "\\\"");
  }
}