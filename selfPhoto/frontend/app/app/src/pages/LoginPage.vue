<script setup lang="ts">
import { debounce, useQuasar } from 'quasar';
import { useUserStore } from 'src/stores/userStore';
import { ref } from 'vue';
import { useI18n } from 'vue-i18n';
import { useRouter } from 'vue-router';

const router = useRouter();
const $q = useQuasar();
const { t } = useI18n();

const emailInput = ref('');
const passwordInput = ref('');

const email = ref(null);
const password = ref(null);

const emailError = ref(false);
const passwordError = ref(false);

const showPassword = ref(false);
const submitting = ref(false);

const userStore = useUserStore();

const submit = async () => {
  if (email.value === null || password.value === null) return;

  if (!email.value.validate()) return;
  if (!password.value.validate()) return;

  submitting.value = true;
  email.value.blur();
  password.value.blur();

  const user: boolean = await userStore.login({
    username: emailInput.value,
    password: passwordInput.value,
  });

  if (!user) {
    console.log('Invalid');
    return;
  }

  // await userStore.loadAssets({});

  router.push({ path: '/' });
};

const handlePasswordReset = () => {
  if (!email.value.validate()) return;

  submitting.value = true;
  email.value.blur();
  password.value.blur();

  userStore.passwordReset(emailInput.value);

  $q.dialog({
    title: t('passwordResetNotificationTitle'),
    message: t('passwordResetNotificationBody'),
  }).onDismiss(() => {
    submitting.value = false;
  });
};
</script>

<template>
  <q-page
    class="bg-white window-full window-width row justify-center items-center"
  >
    <div class="column col-9" style="max-width: 500px">
      <q-card square bordered class="q-pa-xl shadow-0">
        <q-card-section class="text-center">
          <div class="text-h5 text-weight-regular">Sign in</div>
          <div class="text-subtitle1 q-mt-sm">to continue to Your Photos</div>
        </q-card-section>
        <q-card-section>
          <q-form class="q-gutter-md q-pb-sm" autofocus>
            <q-input
              ref="email"
              :disable="submitting"
              outlined
              bottom-slots
              lazy-rules="ondemand"
              v-model="emailInput"
              type="email"
              label="Email"
              :rules="[(val) => !!val || $t('emailPrompt'), 'email']"
              @change="debounce(email.resetValidation(), 100)"
              @keyup.enter="submit"
            />
            <q-input
              ref="password"
              :disable="submitting"
              outlined
              bottom-slots
              lazy-rules="ondemand"
              v-model="passwordInput"
              :type="showPassword ? 'text' : 'password'"
              label="Password"
              @keyup.enter="submit"
              :rules="[(val) => !!val || $t('passwordPrompt')]"
              @change="debounce(password.resetValidation(), 100)"
            >
              <template v-slot:append>
                <q-icon
                  :name="showPassword ? 'visibility' : 'visibility_off'"
                  class="cursor-pointer"
                  @click="showPassword = !showPassword"
                />
              </template>
            </q-input>
          </q-form>
          <q-btn flat class="text-primary" @click="handlePasswordReset">
            {{ $t('forgotPassword') }}
          </q-btn>
        </q-card-section>
        <q-card-actions class="q-px-md q-pt-xl" align="between">
          <q-btn
            flat
            no-caps
            color="blue"
            size="md"
            class="item-right"
            :label="$t('createAccount')"
            type="button"
          />

          <q-btn
            unelevated
            no-caps
            color="blue"
            size="md"
            :label="$t('login')"
            type="submit"
            padding="5px 20px"
            :loading="submitting"
            @click="submit"
          >
            <template v-slot:loading>
              <q-spinner-facebook />
            </template>
          </q-btn>
        </q-card-actions>
      </q-card>
    </div>
  </q-page>
</template>

<style scoped>
.card {
  width: 75%;
}
</style>
