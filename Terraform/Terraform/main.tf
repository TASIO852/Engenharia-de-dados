##################################
###### DATABRICKS RESOURCES ######
##################################
resource "databricks_pipeline" "this" {

  cluster {
    label = "default"
    aws_attributes {
      instance_profile_arn = "arn:aws:iam::584991916600:instance-profile/databricks-workspace-stack-access-data-buckets"
    }
    autoscale {
      min_workers = 2
      max_workers = 12
      mode        = "ENHANCED"
    }
    custom_tags = {
      cluster_type = "default"
    }
  }

  cluster {
    label = "maintenance"
    aws_attributes {
      instance_profile_arn = "arn:aws:iam::584991916600:instance-profile/databricks-workspace-stack-access-data-buckets"
    }
    num_workers = 1
    custom_tags = {
      cluster_type = "maintenance"
    }
  }

  library {
    notebook {
      path = var.bw_etl_vendas_notebook_path
    }
  }

  development = true
  continuous  = false
  channel     = "CURRENT"
  edition     = "ADVANCED"
  photon      = true

  name    = join("-", [var.pipeline_name, var.env])
  storage = "dbfs:/pipelines/173ca49a-de63-4bde-84de-5fc57c45df38"
  target  = "default"

}
