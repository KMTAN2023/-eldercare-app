cd "c:/Program Files/KNIME"
knime.exe -nosplash -nosave -reset -application org.knime.product.KNIME_BATCH_APPLICATION -workflowDir="C:/OR_Project/OptiRoute/Data/data_model/01_DataPrep" 

cd C:\OR_Project\OptiRoute\ProjectRun
dotnet OptiRoute.dll

cd "c:/Program Files/KNIME"
knime.exe -nosplash -nosave -reset -application org.knime.product.KNIME_BATCH_APPLICATION -workflowDir="C:/OR_Project/OptiRoute/Data/data_model/02_output_transform" 