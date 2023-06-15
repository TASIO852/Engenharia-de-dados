#################################
###### UNIVERSAL VARIABLES ######
#################################
variable "env" {
  description = "Environment where this module is invoked."
  type        = string
  default     = ""
}


##################################
###### DATABRICKS VARIABLES ######
##################################
variable "pipeline_name" {
  description = "A name for the pipeline."
  type        = string
  default     = "My pipeline"
}

variable "bw_etl_vendas_notebook_path" {
  description = "path to bw_etl_vendas connect notebook"
  type        = string
}
