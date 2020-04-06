package eu.rienafairefr.customcodegen;

import org.apache.commons.io.FileUtils;
import org.openapitools.codegen.ClientOptInput;
import org.openapitools.codegen.DefaultGenerator;
import org.openapitools.codegen.config.CodegenConfigurator;

import java.io.File;

public class EntryPoint {
    public static void main(String[] args) {
        File outputDir = new File(args[1]);
        FileUtils.deleteQuietly(outputDir);

        CodegenConfigurator configurator;
        ClientOptInput clientOptInput;
        DefaultGenerator generator = new DefaultGenerator();

        configurator = new CodegenConfigurator()
                .setGeneratorName(PythonCustomCodegen.class.getName()) // use this codegen library
                .setPackageName("truelayer")
                .setTemplateDir("../templates")
                .setInputSpec(args[0])
                .setOutputDir(args[1]);

        clientOptInput = configurator.toClientOptInput();
        generator.opts(clientOptInput).generate();
    }
}
