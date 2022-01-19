# cicd_python
python Непрерывная интеграция и доставка

```bash
docker build -t jenkins-python .

docker run --rm -p 8080:8080 -p5000:5000 -v jenkins_home:/var/jenkins_home jenkins-python
```