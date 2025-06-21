output "ec2_public_ip" {
  value = aws_instance.fastapi.public_ip
}

output "rds_endpoint" {
  value = aws_db_instance.postgres.endpoint
}

output "redis_endpoint" {
  value = aws_elasticache_cluster.redis.cache_nodes[0].address
}
